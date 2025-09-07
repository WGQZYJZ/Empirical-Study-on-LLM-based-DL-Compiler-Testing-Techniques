
model = torch.nn.Sequential(
    torch.nn.Conv2d(3, 64, kernel_size=1), 
    torch.nn.Flatten(),
    torch.nn.Dropout(.5))

# Initializing the model
m  = model

 # Inputs to the model