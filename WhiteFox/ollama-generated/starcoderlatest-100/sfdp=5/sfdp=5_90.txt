
class SelfAttnModel(torch.nn.Module):
    def __init__(self, d_model: int = 512, nhead: int = 8):
        super().__init__()

        # This layer computes the dot products between query and key (query + attn_mask)
        self.attn_layer = torch.nn.Linear(d_model, d_model, bias=False)
        
        # Self-attention module 
        # We need to project the d_model back into dim for inputting as the value in FFN
        self.self_attn_layer = torch.nn.Linear(d_model, d_model * 2, bias=False)
 
        # This layer computes the FFN result (FFN_output = x + conv1x1 + relu(conv1x1) + conv2x1 + relu(conv2x1))
        self.fc1 = torch.nn.Linear(d_model * 4, d_model)
        
        # This layer converts FFN output into logits (logits = fc1x + relu(fc1x)) and applies dropout to the result
        self.fc2 = torch.nn.Linear(d_model, d_model)

        # Softmax normalization layer
        self.norm = torch.nn.LayerNorm(d_model)
        
        # Dropout operation for final output
        self.drop = torch.nn.Dropout(dropout_p)
 
    def forward(self, x):
        qk = self.attn_layer(x).view(-1, x.shape[-2], x.shape[-1])  # [bs * sl * hs] -> [bs * sl * d_model / h] -> [sl * bs * d_model / h]
        
        # Apply self attention with softmax
        attn = torch.softmax(qk @ qk.transpose(-2, -1) / math.sqrt(qk.size(-1)), dim=-1).view(*x.shape[:-2], x.shape[-2], x.shape[-1])  # [sl * bs * d_model / h] -> [bs * sl * d_model / h]
        
        qkv = self.self_attn_layer(x)
        qkv = self.drop(torch.cat([qkv[:, :x.shape[-2], :], x, qkv[:, x.shape[-2]:]], dim=-1))

        # Apply final FFN block with 4 linear layers and a relu activation function for each layer
        ffn_output = (attn @ qkv).transpose(-2, -1).contiguous().view(*x.shape[:-2], -1)
        
        logits = self.fc1(ffn_output) + self.fc2(self.drop(torch.tanh(logits)))

        # Apply layer normalization and dropout operation on the output
        x = self.norm(logits).unsqueeze(-1)
        
        return self.drop(x)


# Initializing the model
m = SelfAttnModel()

# Inputs to the model
x = torch.randn(1, 32, 1024, dtype=torch.float32)
