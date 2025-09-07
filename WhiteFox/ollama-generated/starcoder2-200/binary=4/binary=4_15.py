

model = torch.nn.Sequential()

linear1 = torch.nn.Linear(2048, 5) # Applying a linear transformation to the input vector of length 2048 with an output vector of length 5

model.add(linear1)


## model.add(torch.nn.Flatten(start_dim=1))
## model.add(torch.nn.Tanh())


linear2 = torch.nn.Linear(3, 4096 * 7 * 7) # Applying another linear transformation to the output of a flatten layer with an output vector that is 4096 * 7 * 7

model.add(linear2)

