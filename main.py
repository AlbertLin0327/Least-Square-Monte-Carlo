# Import Black Scholes Model
from LeastSquaresMonteCarlo import LSMC


# Estimate Delta by drifting the random path
def estimate_delta(Model, dS):

    price = Model.Price

    # Shift the path
    Model.randomWalk *= 1 + dS

    # pricing
    Model.pricing()

    Delta = (Model.Price - price) / (Model.spot_price * dS)

    print("")
    print("-----------------------------")
    print(f"Price of {Model.type} after {dS} shift: {Model.Price}")
    print(f"Stdandard deviation after {dS} shift: {Model.std}")
    print(f"Root Mean Sqaure Relative Error after {dS} shift: {Model.rmsre}")
    print(f"Estimated Delta of {Model.type}: {Delta}")
    print("-----------------------------")
    print("")


# main function
def main():

    # Determine the type of American Option
    print("Enter the type of American Option, Put or Call")

    while True:
        type = input(">>> ").lower()

        if type == "put" or type == "call" or type == "p" or type == "c":
            type = type[0]
            break

        print("Enter Put or Call!!!")

    # take in the input from user
    print("")
    print(
        "Enter: spot price, strike price, time interval, interest(%), dividend(%), volatility(%), period, stimulations"
    )

    while True:
        try:
            (
                spot,
                strike,
                time,
                interest,
                dividend,
                volatility,
                period,
                simulations,
            ) = map(float, input(">>> ").split())
            break

        except:
            print("WRONG FORMAT!!!")

    Model = LSMC(
        type, spot, strike, time, interest, dividend, volatility, period, simulations
    )

    # Calculating Price
    Model.random_path()
    Model.pricing()

    type = "Put" if type == "p" else "Call"

    print("")
    print("-----------------------------")
    print(f"Price of {type}: {Model.Price}")
    print(f"Stdandard deviation: {Model.std}")
    print(f"Root Mean Sqaure Relative Error: {Model.rmsre}")
    print("-----------------------------")
    print("")

    print(Model.randomWalk[:, -1])

    # Plot distribution
    Model.plot()

    print(
        "Enter the dS (porportion) to shift the Random Path to estimate delta. Better to have 0 < dS <= 0.1"
    )

    while True:
        try:
            dS = float(input(">>> "))
            break

        except:
            print("Invalid Input!!!")

    estimate_delta(Model, dS)


if __name__ == "__main__":
    main()
