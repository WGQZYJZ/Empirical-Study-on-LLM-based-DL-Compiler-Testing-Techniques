
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 2)
 
    def forward(self, input1, input2):
        t1 = torch.cat([input1, input2], dim=1) # Concatenate input tensors along dimension 1
        t2 = t1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        t3 = t2[:, 0:input_tensor.size(1)] # Further slice the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1) 
        v1  = self.fc(t4).argmax(dim=-1)
        return v1


# Initializing the model