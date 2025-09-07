
class AttentionModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, num_heads):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            embed_dim=input_dim, num_heads=num_heads)
        self.linear1 = torch.nn.Linear(hidden_dim, 2*input_dim)
        self.linear2 = torch.nn.Linear(2*input_dim, input_dim)
 
    def forward(self, x1):
        qk = self.attention(x1, x1, x1)[0]
        v = self.attention(x1, x1, x1)[1]
        # print("qk size:", qk.shape)
        # print("v size:", v.shape)
 
        # concatenate the output of MultiheadAttention and linear layer 2 and apply linear layer 1 to obtain the attn_output 
        attn_output = torch.cat([qk, v], dim=-1)
        # print(attn_output.shape)
        attn_output = self.linear1(attn_output)
        attn_output = F.relu(attn_output)
        attn_output = self.linear2(attn_output)
 
        return attn_output
 
# Initializing the model
m = AttentionModel(3, 8, 4)

 # Inputs to the model
x1 = torch.randn(1, 64, 64)
