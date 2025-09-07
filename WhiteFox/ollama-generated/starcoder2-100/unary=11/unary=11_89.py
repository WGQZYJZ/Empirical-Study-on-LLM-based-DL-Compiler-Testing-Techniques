t1 = torch.nn.Sequential(
    torch.nn.Conv2d(32, 64, kernel_size=7),
    torch.nn.ReLU(), 
    torch.nn.MaxPool2d(kernel_size=2)
)
