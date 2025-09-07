
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
       t3 = torch.relu(t1 + t2)  # Concatenate t1 and t2 then apply ReLU to the resulting tensor.
       return t3

# Initializing the model
m = Model()

