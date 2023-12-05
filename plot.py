import matplotlib.pyplot as plt

if __name__ == "__main__":
    func = ["DP", "BnB"]
    input_sizes = [[10000, 100000, 1000000], [100, 300, 900]]
    memory = [[320, 10192, 101876], [260, 264, 1804]]
    times = [[0.011, 0.132, 1.396], [0.004, 0.061, 600]]
    # Add more sizes as needed

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(input_sizes[0], times[0], label=func[0])
    ax1.set_xlabel('Size of N')
    ax1.set_ylabel('Running Time (s)')
    ax1.set_title('Dynamic Programming, MVC')
    ax1.legend()
    
    ax2.plot(input_sizes[1], times[1], label=func[1], color='red')
    ax2.set_xlabel('Size of N')
    ax2.set_ylabel('Running Time (s)')
    ax2.set_title('Branch and Bound MVC')
    ax2.legend()

    plt.show()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(input_sizes[0], memory[0], label=func[0])
    ax1.set_xlabel('Size of N')
    ax1.set_ylabel('Memory Usage (KB)')
    ax1.set_title('Dynamic Programming MVC')
    ax1.legend()
    
    ax2.plot(input_sizes[1], memory[1], label=func[1], color='red')
    ax2.set_xlabel('Size of N')
    ax2.set_ylabel('Memory Usage (KB)')
    ax2.set_title('Branch and Bound MVC')
    ax2.legend()

    plt.show()