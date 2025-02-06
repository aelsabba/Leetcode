class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_num = (hour % 12 + minutes / 60) * 360 / 12
        minute_num = minutes * 360 / 60
        diff = abs(hour_num - minute_num)
        diff2 = 360 - diff
        return min(diff,diff2)