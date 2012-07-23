module Codebreaker
  class Marker
    def initialize(secret, guess)
      @secret = secret
      @guess = guess
    end

    def number_match_count
      total_match_count - exact_match_count
    end

    def total_match_count
      secret = @secret.chars.to_a
      @guess.chars.to_a.inject(0) do |count, g|
        count + (delete_first(g, secret) ? 1 : 0)
      end
    end

    def delete_first(c, code)
      code.delete_at(code.index(c)) if code.index(c)
    end

    def exact_match_count
      total_matches(:exact_match?)
    end

    def total_matches(method)
      (0..3).inject(0) do |count, index|
        count + (send(method, index) ? 1 : 0)
      end
    end

    def number_match?(index)
      @secret.include?(@guess[index]) && !exact_match?(index)
    end

    def exact_match?(index)
      @secret[index] == @guess[index]
    end
  end
end