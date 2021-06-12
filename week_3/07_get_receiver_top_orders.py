top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    height_len = len(heights)
    answer = [0] * height_len
    while heights :
        height = heights.pop()
        for index in range(height_len - 1, -1, -1) :
            if heights[index] > height :
                answer[len(heights)] = index + 1
                break

    return answer



print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!