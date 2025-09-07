
class SelfAttentionModule(torch.nn.Module):
    def __init__(self, num_attention_heads, input_dim, intermediate_size, hidden_dropout_prob, layer_norm_eps=1e-5):
        super().__init__()

        self.self_attn = torch.nn.MultiheadAttention(embed_dim=input_dim, num_heads=num_attention_heads)
        self.layer_norm  = torch.nn.LayerNorm(input_dim, eps=layer_norm_eps)
        self.ffn         = torch.nn.Linear(intermediate_size + input_dim, input_dim)
        self.dropout     = torch.nn.Dropout(hidden_dropout_prob)
 
    def forward(self, x):
        attn_output, _ = self.self_attn(x, x, x) # Apply multi-head attention to the query, key, and value tensor outputs
        ffn_input    = torch.cat([attn_output, x], dim=-1)
        ffn_output   = F.relu(self.ffn(ffn_input))
        return self.dropout(attn_output + self.layer_norm(x))

class Model(torch.nn.Module):
    def __init__(self, input_dim=2048, intermediate_size=768, num_attention_heads=12, hidden_dropout_prob=0.1):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 32, kernel_size=(5, 5), stride=(2, 2)) # Convolution (46, 57) -> (28, 28)
        self.attention_module   = SelfAttentionModule(num_attention_heads=num_attention_heads, input_dim=input_dim, intermediate_size=intermediate_size, hidden_dropout_prob=hidden_dropout_prob)
        self.layer_norm = torch.nn.LayerNorm(2048 + 32)
        self.fc1        = torch.nn.Linear(2048 + 32, intermediate_size) # Flatten to (192, 768) -> (192, 3072), linear layer and dropout
        self.relu       = torch.nn.ReLU() # ReLU activation
        self.fc2        = torch.nn.Linear(intermediate_size, 2048) # Dropout to (192, 2048) -> (192, 2048), linear layer and dropout
        self.dropout    = torch.nn.Dropout(hidden_dropout_prob)
 
    def forward(self, x):
        v1 = F.relu(self.conv(x)) # Convolution to (16, 16) -> (9, 9)

        v2 = v1 * 0.5         # Scale the output of the convolution by 0.5
        v3 = v1 * 0.70710678  # Multiply the output of the convolution by 0.70710678
        v4 = torch.erf(v3)    # Apply the error function to the output of the convolution
        v5 = v4 + 1           # Add 1 to the output of the error function
        v6 = v2 * v5          # Multiply the output of the convolution by the output of the error function

        attn_input     = torch.cat([v6, x], dim=-1) # Concatenate the scaled and output of the convolution with the input tensor
        attention_output = self.attention_module(attn_input) # Apply a multi-head attention module to the concatenated scaled and output of the convolution
        ffn_input      = torch.cat([attention_output, v6], dim=-1) # Concatenate the output of the multi-head attention with the scaled and output of the convolution
        ffn_output     = self.relu(self.fc1(ffn_input)) # Apply an ReLU activation to the concatenated input tensor of the multi-head attention and the scaled and output of the convolution

        return self.dropout(ffn_output + self.layer_norm(attn_input)) # Dropout and add Layer Normalization between the concatenation of the scaled and output of the convolution and the input tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
