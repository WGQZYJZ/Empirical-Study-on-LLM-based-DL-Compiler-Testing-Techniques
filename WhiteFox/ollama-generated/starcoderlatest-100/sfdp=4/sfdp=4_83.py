
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, nhead=1, dim_model=512):
        super().__init__()
        self.dim_model = dim_model
        self.nhead = nhead
 
    def forward(self, query, key, value, attn_mask):
        # Compute the dot product of the query and key, and scale it
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        # Add the attention mask to the scaled dot product
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        # Compute the dot product of the attention weights and the value
        output = attn_weight @ value

        return output
 
 class MultiHeadAttnModule(torch.nn.Module):
     def __init__(self, nhead=8, dim_model=512):
         super().__init__()
         self.nhead = nhead
         self.attn = MultiHeadAttention(self.nhead, dim_model)
 
         # 8 * 64 * 64 --> 8 x 64 x 64
        self.fc1 = torch.nn.Linear(dim_model * 2, dim_model * 4)
 
        # 8 x 64 x 64 --> 8 x 512
        self.ln = torch.nn.LayerNorm(dim_model * 4)
 
     def forward(self, query, key, value):
         attn_output = self.attn(query, key, value)
         # Concatenate the values and attention weights to produce the output tensor
         output = torch.cat((attn_output, value), dim=1)
         output = self.fc1(output)
         output = F.relu_(output)
         output = output @ self.ln.weight.T
         return output
 
 class Model(torch.nn.Module):
     def __init__(self, dim_model=512):
         super().__init__()
 
         # 3 x 64 * 64 --> 8 x 64 x 64
         self.conv = torch.nn.Conv2d(3, 8, 3)
 
         self.attn_module1 = MultiHeadAttnModule()
 
 
         # 8 x 64 x 64 --> 8 x 512
         self.ln = torch.nn.LayerNorm(dim_model * 4)
 
         # 512 -> 3 x 64 * 64
        self.conv1 = torch.nn.ConvTranspose2d(dim_model * 4, 3, 3)
 
     def forward(self, input):
         v1 = F.relu_(self.attn_module1(input))  # (8 x 64 x 64) -> (8 x 512)
         v2 = self.ln(v1)  # (8 x 512) -> (8 x 64 x 64)
         v3 = torch.transpose(v2, -1, -2)  # (8 x 64 x 64) -> (8 x 64 x 512)
         out = F.relu_(self.conv1(v3)) + self.conv(input)  # input: (3 x 64 x 64); output:(3 x 64 x 64)
         return out
 
 
 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
