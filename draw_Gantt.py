import matplotlib.pyplot as plt

def draw_schedule(values):
    unique_values = list(set(values))
    unique_values.sort()
    colors = plt.cm.tab20.colors

    value_color_map = {value: colors[i % len(colors)] for i, value in enumerate(unique_values)}

    fig, ax = plt.subplots()
    y_pos = 5

    for idx, value in enumerate(values):
        ax.barh(y_pos, 1, left=idx, color=value_color_map[value], height=0.8)

    ax.set_title('Scheduling Gantt chart')
    ax.legend([plt.Rectangle((0, 0), 1, 1, fc=value_color_map[val]) for val in unique_values], unique_values)

    ax.set_ylim(0,10)

    plt.show()

