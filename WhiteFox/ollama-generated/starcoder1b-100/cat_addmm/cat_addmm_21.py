
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(5, 2)
        self.fc2 = torch.nn.Linear(2, 10)
 
    def forward(self, x):
        t1 = torch.addmm(x, x, x)  # Perform matrix multiplication of itself and itself and add it to a tensor
        t2 = torch.cat([t1], dim=-1)  # Concatenate the result along the first dimension (time dimension). We don't need to specify axis because we just concatenate time dimension together for our model.
        return self.fc2(t2)


# Initializing the model
m = Model()


