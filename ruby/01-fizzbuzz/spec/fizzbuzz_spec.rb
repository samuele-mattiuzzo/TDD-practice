require './lib/fizzbuzz.rb'

RSpec.describe FizzBuzz do
    let(:fizzbuzz) { described_class.new(1) }
    describe 'initializing' do
        it 'creates a new instance' do
            expect(fizzbuzz).to be_instance_of(FizzBuzz)
        end
    end
  end
