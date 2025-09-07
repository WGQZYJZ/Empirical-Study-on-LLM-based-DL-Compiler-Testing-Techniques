__builtins__.print('Your model class should inherit torch.nn.Module or torch.nn.Sequential class.')

class Model(torch.nn.Module):
    def __init__(self, inputSize=2, outputSize=4096):
        super().__init__()

        self.linear1 = torch.nn.Linear(inputSize, 5) # The number of input features must be >= 1 and <= output_size 
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(outputSize - 3072 , 496*2) 
        self.linear3 = torch.nn.Linear(inputSize, inputSize + 5)
        self.relu1 = torch.nn.ReLU()
        self.linear4 = torch.nn.Linear(512*2, 8) 
        self.softmax = torch.nn.Softmax(dim=0)
    def forward(self, x):
        v3 = self.linear3(x).permute(0, 3, 1) # This pattern characterizes scenarios where the permute function is invoked.
        return self.linear4(v3)

# Initialization of Model 
model = Model()
print('Your model should have at least one call to permute() or its variants.')

print('This line below must appear in your code:')
print('
