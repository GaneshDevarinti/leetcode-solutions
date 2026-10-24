class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_days(date_str: str) -> int:
      month, day = map(int, date_str.split("-"))
      return sum(days_in_months[: month - 1]) + day

    start_a = to_days(arriveAlice)
    end_a = to_days(leaveAlice)
    start_b = to_days(arriveBob)
    end_b = to_days(leaveBob)

    start_overlap = max(start_a, start_b)
    end_overlap = min(end_a, end_b)

    return max(0, end_overlap - start_overlap + 1)
