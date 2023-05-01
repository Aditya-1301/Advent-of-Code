defmodule D do
  def rf do
    file = "D:\\Elixir\\AdventOfCode2022inElixir\\Day1\\input1.txt"
    {:ok, input} = File.read(file)
    elves = String.split(input, "\r\n\r\n")
    sums = []
  end

  def calcSum([head], max, acc) do # def calcSum([head], max, sums) do
    s = String.split(head, "\r\n")
    value = calcElf(s, 0)
    cond do
        value > max -> value; acc = [value|acc]
        value < max -> max; acc = [max|acc]
    end
  end

  def calcSum([head | rest], max, acc) do # def calcSum([head|rest], max, sums) do
    s = String.split(head, "\r\n")
    value = calcElf(s, 0);
    #sums = addToList(value,sums)
    if value > max do
      calcSum(rest, value) #calcSum(rest, value, sums)
    else
      calcSum(rest, max) #calcSum(rest, max, sums)
    end
  end

  def calcElf([head], sum) do
    case head do
      "" -> sum
      _  -> i = String.to_integer(head); sum + i
    end
  end

  def calcElf([head|rest], sum) do
    case head do
      "" -> sum
      _  -> i = String.to_integer(head); calcElf(rest, sum + i)
    end
  end
end
