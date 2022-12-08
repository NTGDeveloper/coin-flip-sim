import random

# Initialize Variables
flip_list = list()
flip_times = 0
heads_count = 0
tails_count = 0

def simulate_coin_flips(verbose_mode, flip_list):
  flip = random.randint(1,2)
  flip_list.append(flip)
  if verbose_mode == True:
    if flip == 1:
      print("#" + str(flip_times) + " - HEADS")
    if flip == 2:
      print("#" + str(flip_times) + " - TAILS")
  return flip_list


# Asking for Parameters
times = int(input("How many times would you like to run the test? "))
verbose_mode = input("Verbose Mode? 'True/False' ")

if verbose_mode == "True" or verbose_mode == "true":
  verbose_mode = True
else:
  verbose_mode = False

# Looping based on how many times were specified
for x in range(0, times):
  flip_times += 1
  flip_list = simulate_coin_flips(verbose_mode, flip_list)
  if flip_list[-1] == 1:
    heads_count += 1
  if flip_list[-1] == 2:
    tails_count += 1

#Cleans environment
if verbose_mode == True:
  print("")
  print("")

print("")

# Calculating Avg. Percentages
percentage_heads = (heads_count / times) * 100
percentage_tails = (tails_count / times) * 100

# Displaying Results
print("Number of flips: " + str(times))
print("")
print("Percentage Heads: " + str(percentage_heads) + "%")
print("Percentage Tails: " + str(percentage_tails) + "%")
print("")
print("Number of Heads: " + str(heads_count))
print("Number of Tails: " + str(tails_count))