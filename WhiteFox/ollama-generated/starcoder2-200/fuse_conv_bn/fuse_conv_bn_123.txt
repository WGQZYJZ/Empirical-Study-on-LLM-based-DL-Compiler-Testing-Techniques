
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 5, 3)

    def forward(self, x1):
       return torch.nn.functional.batch_norm(
            torch.nn.functional.conv2d(x1, weight, bias), 
            torch.nn.functional.relu(torch.nn.functional.max_pool2d(x1)))

# Initializing the model
m = Model()
# Inputs to the model
__output__  = m(__input__)
