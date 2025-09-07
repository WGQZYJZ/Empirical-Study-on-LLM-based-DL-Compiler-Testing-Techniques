
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Concatenate 3 tensors of size (b1, 50) along the first dimension.
        v1 = torch.cat([x1[:, :48], x1[:,-1].view(-1,1), x1[:, -1:]], dim=1)

        # Reshape the concatenated tensor to be of shape b1 * (4 + 50 + 2).
        v2 = v1.view(v1.size()[0]*(4+50+2))

        # Apply ReLU unary operator to the reshaped tensor.
        v3 = torch.relu(v2)

        return v3

# Initializing the model:
m  = Model()
