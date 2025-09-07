
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        query = self.linear(x).squeeze(-1)  # Remove the batch dimension of the query tensor
        key = self.linear(x).squeeze(-1)  # Remove the batch dimension of the key tensor
        value = torch.randn_like(x)  # Randomly initialize the result tensor
        scale_factor = torch.exp(self.linear(x)) / torch.norm(x, dim=-1, keepdim=True)  # Initialize a scaling factor
        softmax = torch.nn.functional.softmax(query, dim=-1)
        dropout = torch.nn.functional.dropout(softmax, p=0.3)
        result = torch.tanh(dropout.matmul(value)) * scale_factor  # Add a term to the attention map
        return result


# Initializing the model
m = Model()


