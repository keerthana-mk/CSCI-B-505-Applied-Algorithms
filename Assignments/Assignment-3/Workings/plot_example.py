import csv
import matplotlib.pyplot as plt


if __name__ == '__main__':

  data = []
  location_name = input("file: ")

with open(location_name, 'r') as f:
   fcsv = csv.reader(f)
   for lines in fcsv:
        data.append(list(map(int, lines)))

print(data)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.title("Data Plot")
X,Y = [],[]
for x,y in data:
        X.append(x**2)
        Y.append(y)

plt.scatter(X,Y)

new_location_name = input("file: ")
plt.savefig(new_location_name, dpi=300, bbox_inches='tight')
plt.show()