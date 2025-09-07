
class Model(torch.nn.Module):
    def __init__(self, num_features1=4096, num_features2=576):
        super().__init__()
 
        self.dense = torch.nn.Linear(num_features1, num_features2)
 
    def forward(self, x):
 
        return self.dense(x), torch.cat([x], 3)

# Initializing the model
m = Model()


# Inputs to the model