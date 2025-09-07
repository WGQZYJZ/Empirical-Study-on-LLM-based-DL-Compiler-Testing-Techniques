
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v = torch.cat(input_tensors, dim=1)[:, 0:9223372036854775807][:size] # Modify this line only!!!
        return v

# Initializing the model
m = Model()

