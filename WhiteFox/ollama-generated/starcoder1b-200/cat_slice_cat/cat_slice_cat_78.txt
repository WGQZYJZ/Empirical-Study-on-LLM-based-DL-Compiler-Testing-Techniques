
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor1, input_tensor2):
        v1 = torch.cat((input_tensor1, input_tensor2), dim=1)  # Concatenate the two input tensors along dimension 1
        v2 = v1[:, :8]    # Slice the concatenated tensor along dimension 1
        v3 = v2[:4096]   # Further slice the tensor along dimension 1
        return torch.cat((input_tensor1, input_tensor2), dim=1)


# Initializing the model
m = Model()


