

model = nn.Sequential(*[
    nn.Conv2d(3,8,1), 
    *nn.Linear(3*32*32, 48),
    nn.ReLU(),
    
    *nn.Linear(48,16),
    nn.Sigmoid(),

    *nn.Linear(16,7),
    nn.Softmax()
])

inputs = torch.rand(size=(90,3,5))

__output__  = model(inputs)