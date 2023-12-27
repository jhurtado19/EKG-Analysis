

## Calculating Power 

def linreg(name, weight, left, right):
 array = np.loadtxt(f"/content/gdrive/MyDrive/Lab 7/Group 6/Final Project Data/final_{name.lower()}_{weight}.csv", delimiter=',')[left:right]
 time = (array[:,0] - array[0][0])/1000
 distance = (array[:,1] - array[0][1])/100
 fig, axs = plt.subplots(2)
 axs[0].plot(distance)
 axs[1].plot(time, distance)
 results, cov = np.polyfit(time, distance, 1, cov = True)
 model = time* results[0] + results[1]
 axs[1].plot(time, model)
 print(f"Slope: {results[0]} ± {np.sqrt(cov[0][0])} m/s")
 force = (weight * 0.453592) * 9.81
 print(f"Force: {force}")
 power = force * results[0]
 d_power = power * np.sqrt(cov[0][0])/results[0]
 print(f"Power: {power} ± {d_power}")
