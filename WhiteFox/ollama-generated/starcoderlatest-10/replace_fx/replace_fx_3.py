
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.nn.functional.softmax(v1, dim=-1).unsqueeze(-1) # A tensor with shape (batch_size, input_tensor_shape[-2], ..., input_tensor_shape[-3]) and the last dimension has only one element as 1, for all elements of batch_size
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 5, 6)
