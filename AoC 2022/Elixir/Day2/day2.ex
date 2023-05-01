defmodule D2 do
  def readFile do
    file = "input2.txt"
    {:ok, input} = File.read(file)
    lines = String.split(input, "\r\n")
    IO.inspect(iterate(lines, 0))
    IO.inspect(iterate2(lines, 0))
  end

  def iterate([], sum) do
    sum
  end
  def iterate([head|rest], sum)do
    increment = case head do
      "A X" -> 1+3
      "A Y" -> 2+6
      "A Z" -> 3+0
      "B X" -> 1+0
      "B Y" -> 2+3
      "B Z" -> 3+6
      "C X" -> 1+6
      "C Y" -> 2+0
      "C Z" -> 3+3
    end
    iterate(rest,sum+increment)
  end

  def iterate2([], sum) do
    sum
  end
  def iterate2([head|rest], sum)do
    increment = case head do
      "A X"->3+0
      "A Y"->1+3
      "A Z"->2+6
      "B X"->1+0
      "B Y"->2+3
      "B Z"->3+6
      "C X"->2+0
      "C Y"->3+3
      "C Z"->1+6
    end
    iterate2(rest,sum+increment)
  end
end
