
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.key = torch.nn.Parameter(
            torch.randn(1024, 384), requires_grad=True)
        self.query = torch.nn.Parameter(
            torch.randn(1024, 576), requires_grad=True)
        self.value = torch.nn.Parameter(torch.randn(1024, 384))
 
    def scaled_dot_product(self, query: torch.Tensor):
        key = self.key.unsqueeze(dim=0).repeat(
            query.size(0), 1, 1)
        return torch.matmul(query, key.transpose(-2, -1))
 
    def softmax(self, dim=-1):
        softmax_out = F.softmax(self.scaled_dot_product(self.query), dim=dim)
        return softmax_out
 
    def forward(self, x1):
        attention_weights = self.softmax(dim=-1)
        output = torch.matmul(attention_weights, self.value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 384, 64, 64)
