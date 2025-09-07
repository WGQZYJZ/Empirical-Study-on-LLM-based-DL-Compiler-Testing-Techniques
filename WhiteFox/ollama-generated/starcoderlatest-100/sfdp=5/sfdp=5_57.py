
class Model(torch.nn.Module):
    def __init__(self, input_size=1024, nhead=8, num_attention_heads=16, hidden_dim=512):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(input_size, nhead, num_attention_heads, 
                                                    dropout_p=0, batch_first=False)
        self.fc1 = torch.nn.Linear(hidden_dim, hidden_dim * 2)

    def forward(self, x):
        attn_output = self.attn(x)[0] # Get the output of the attention mechanism
        attn_output = F.gelu(attn_output)
        output = torch.matmul(attn_output, self.attn.weight.transpose(-2, -1))
        output = torch.cat((attn_output, output), dim=-1)
        output = self.fc1(output)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 32, 512, requires_grad=True)
