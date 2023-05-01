defmodule MixpTest do
  use ExUnit.Case
  doctest Mixp

  test "greets the world" do
    assert Mixp.hello() == :world
  end
end
