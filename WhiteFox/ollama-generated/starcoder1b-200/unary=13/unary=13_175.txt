
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 8)
 
    def forward(self, x1):
        v1 = F.relu(self.linear(x1))  # Apply the rectified linear transformation to the input tensor
        return F.log_softmax(self.linear(v1), dim=-1)


# Initializing the model
m = Model()


