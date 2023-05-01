defmodule D1 do
  def readFile do
    file = "D:\\Elixir\\AdventOfCode2022inElixir\\Day1\\input1.txt"
    {:ok, input} = File.read(file)
    elves = String.split(input, "\r\n\r\n")
    sums = []
    IO.puts(calcSum(elves, 0)) # IO.puts(calcSum(elves, 0, sums))
    max = sumTop3(elves, {0,0,0})
		sum(max)
  end

  def calcSum([head], max) do # def calcSum([head], max, sums) do
    s = String.split(head, "\r\n")
    value = calcElf(s, 0)
    #sums = addToList(value,sums)
    cond do
        value > max -> value
        value < max -> max
    end
  end

  def calcSum([head | rest], max) do # def calcSum([head|rest], max, sums) do
    s = String.split(head, "\r\n")
    value = calcElf(s, 0);
    #sums = addToList(value,sums)
    if value > max do
      calcSum(rest, value) #calcSum(rest, value, sums)
    else
      calcSum(rest, max) #calcSum(rest, max, sums)
    end
  end

  # def addToList(value, []) do
  #   [value]
  # end

  # def addToList(value, sums) do
  #   sums = Enum.reverse(sums)
  #   sums = [value | sums]
  #   sums = Enum.reverse(sums)
  #   sums
  # end

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

  # def sumTop3(sums) do
  #    Enum.sort(sums, :desc)
  #    Enum.at(sums, 0, nil) + Enum.at(sums, 2 ,nil) + Enum.at(sums, 2, nil)
  # end

  def sumTop3([head], max) do
		ints = String.split(head, "\r\n")
		value = calcElf(ints, 0)
		updateMax(value, max)
	end

	def sumTop3([head|rest], max) do
		ints = String.split(head, "\r\n")
		value = calcElf(ints, 0)
		max = updateMax(value, max)
		sumTop3(rest, max)
	end

  def updateMax(value, {max1, max2, max3}) do
		cond do
			value > max1 -> {value, max1, max2}
			value > max2 -> {max1, value, max2}
			value > max3 -> {max1, max2, value}
			true -> {max1, max2, max3}
		end
	end

	def sum({max1, max2, max3}) do
		max1 +max2 + max3
	end
end
