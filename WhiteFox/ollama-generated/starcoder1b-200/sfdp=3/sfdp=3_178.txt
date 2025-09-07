
class Model(torch.nn.Module):
    def __init__(self, hidden_size, nhead=8):
        super().__init__()
        self.scale = torch.nn.Parameter(
            torch.Tensor([0.13507568984985926]), requires_grad=True)  # Define the scale parameter for attention mechanism
        self.proj_w = torch.nn.Linear(hidden_size, hidden_size, bias=False)  # Define a linear projection layer of the scaled dot product
        self.proj_b = torch.nn.Parameter(torch.zeros((1)))  # Define a bias parameter for projection layer
        self.scale_factor = self.proj_w(self.scale)
        self.softmax_qk = torch.nn.functional.softmax(
            scale_factor, dim=-1)  # Apply softmax to the scaled dot product

    def forward(self, query, key, value):
        query = self.scale_factor * query  # Scale the query by a factor
        query = torch.nn.functional.dropout(query, p=0.5)  # Apply dropout to the scaled dot product

        attn_output = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        attn_output = self.softmax_qk * attn_output  # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(attn_output, p=0.5)  # Apply dropout to the softmax output

        out = torch.matmul(output, value)  # Compute the dot product of the output and the value tensor
        return out


# Initializing the model
m = Model()

