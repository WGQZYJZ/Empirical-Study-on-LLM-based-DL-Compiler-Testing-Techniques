
class Model(torch.nn.Module):
    def __init__(self, d_model=64):
        super().__init__()

        self.d_model = d_model

        # The following line specifies the dimensionality of the query key and value. Please check whether it is compatible with your model.
        self.linear1 = torch.nn.Linear(self.d_model, 2 * self.d_model)
        self.layernorm1 = torch.nn.LayerNorm(self.d_model)

        # Apply linear transformations to the softmax output of the attention mechanism.
        self.linear2 = torch.nn.Linear(self.d_model, d_model)
        self.layernorm2 = torch.nn.LayerNorm(self.d_model)

    def forward(self, x1):
        x1 = self.layernorm1(x1 + self.dropout(self.linear1(x1)))
        attn  = self.softmax(self.linear2(x1))

        output = (attn @ self.value).transpose(0, 1)
        output = output @ self.linear3(output).unsqueeze(-1)
        output = output + x1 # Add back the original input to the result of attention computation

        return output

    def softmax(self, x):
        return torch.nn.functional.softmax(x.permute(0, 2, 1), dim=-1).permute(0, 2, 1)

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 4, self.d_model)
key    = torch.randn(1, 5, self.d_model)
value  = torch.randn(1, 6, self.d_model)
