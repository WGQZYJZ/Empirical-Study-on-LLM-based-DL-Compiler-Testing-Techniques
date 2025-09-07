
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3072, 4096) # Linear layer with input size of 3072 and output size of 4096
        self.dropout_layer = torch.nn.Dropout()
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.dropout_layer(v1) # Applying dropout to the linear layer's output
        return v2

# Initializing the model
m = Model()

