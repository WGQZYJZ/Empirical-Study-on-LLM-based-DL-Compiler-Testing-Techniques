

# Initializing the model
m  = torch.nn.Conv2d(3, 100, kernel_size=4)
m2 = torch.nn.BatchNorm2d(num_features=100)
m  = torch.nn.Sequential(*[m, m2])


# Inputs to the model
x1 = torch.rand((64, 3, 28, 28))

