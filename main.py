# Import Black Scholes Model
from LeastSquaresMonteCarlo import LSMC


# Estimate Delta by drifting the random path
def estimate_delta(Model, dS):

		price = Model.Price

		# Shift the path
		Model.randomWalk *= (1 + dS)

		# pricing
		Model.pricing()

		Delta = (Model.Price - price) / (Model.spot_price * dS)

		print('')
		print('-----------------------------')
		print(f'Price of {dS} shift {Model.type}: {Model.Price}')
		print(f'Stdandard deviation of {dS} shift: {Model.std}')
		print(f'Root Mean Sqaure Error Rate of {dS} shift: {Model.rmser}')
		print(f'Estimated Delta of {dS} shift: {Delta}')
		print('-----------------------------')
		print('')


# main function
def main():

	# Determine the type of American Option
	print("Enter the type of American Option, Put or Call")

	while True:
		try:
			type = input()
			type = type.lower()

			if type == 'put' or type == 'call' or type == 'p' or type == 'c':
				type = type[0]
				break

		except:
			print("Enter Put or Call!!!")


	# take in the input from user
	print('Enter: spot price, strike price, time interval, interest(%), dividend(%), volatility(%), period, stimulations')

	while True:
		try:
			spot, strike, time, interest, dividend, volatility, period, simulations = map(float, input().split())
			break

		except:
			print("WRONG FORMAT!!!")

	Model = LSMC(type, spot, strike, time, interest, dividend, volatility, period, simulations)

	# Calculating Price
	Model.random_path()
	Model.pricing()

	type = 'Put' if type == 'p' else 'Call'

	print('')
	print('-----------------------------')
	print(f'Price of {type}: {Model.Price}')
	print(f'Stdandard deviation: {Model.std}')
	print(f'Root Mean Sqaure Error Rate: {Model.rmser}')
	print('-----------------------------')
	print('')

	print('Enter the dS (porportion) to shift the Random Path to estimate delta. 0 < dS <= 0.1')

	while True:
		try:
			dS = float(input())

			if ds < 0 or ds > 0.1:
				print('Out of resonable estimation region')

			estimate_delta(Model, dS)
			break

		except:
			print(dS)
			print('Invalid Input!!!')

	# Plot distribution
	Model.plot()
	

if __name__ == '__main__':
	main()