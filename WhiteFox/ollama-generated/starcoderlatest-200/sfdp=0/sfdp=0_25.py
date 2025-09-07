
class Model(torch.nn.Module):
    def __init__(self, embed_dim, head_dim, num_heads):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(embed_dim, 1, bias=False)
 
        # Attention Layer
        multihead_attention_layer = torch.nn.MultiheadAttention(embed_dim,
                                                                      head_dim, num_heads)
 
        self.attention_dropout_layer = torch.nn.Dropout(p=0.2)
        self.output_dropout_layer  = torch.nn.Dropout(p=0.2)
        
        # FC layers for key and value
        self.key   = torch.nn.Linear(embed_dim, head_dim * num_heads, bias=False)
        self.value = torch.nn.Linear(embed_dim, head_dim * num_heads, bias=False)
 
    def forward(self, q1, v1):
        # Scaled dot product
        scaled_dot_product = self.scaled_dot_product(torch.cat([q1, k1], dim=-1))
 
        # Softmax of scaled dot product
        attention_weights = torch.nn.Softmax(dim=-1)(scaled_dot_product)
 
        # Multi-head attention layer
        attention_output = multihead_attention_layer(q1, v1, self.attention_dropout_layer(attention_weights))[0]
 
        output = self.key(attention_output).transpose(-2, -1)
        output = torch.nn.Linear(self.num_heads * head_dim, embed_dim)(output)
 
        return attention_weights, attention_output, output


# Initializing the model
model = Model(embed_dim=768, head_dim=128, num_heads=12)
attention_weights, attention_output, output = model(q1=x1, v1=v1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attention_weights, attention_output, output = model(q1=x1, v1=v1)


# Description of requirements
The following model uses the Scaled Dot-Product Attention mechanism with MultiheadAttention layer and Linear layers as its key and value. The MultiheadAttention layer takes `embed_dim` as an input and produces attention vectors of size `(batch_size, embed_dim // num_heads, head_dim)`, which can then be used in the subsequent Fully Connected Layer for key/value vectors.

class Model(torch.nn.Module):
    def __init__(self, embed_dim, head_dim, num_heads):
        super().__init__()
 
        # MultiheadAttention layer
        multihead_attention_layer = torch.nn.MultiheadAttention(embed_dim,
                                                                      head_dim, num_heads)
 
    def forward(self, q1, v1):
        attention_output = multihead_attention_layer(q1, v1)[0]
 
        return attention_output
 

# Initializing the model
model = Model(embed_dim=768, head_dim=128, num_heads=12)
attention_output = model(q1=x1, v1=v1)

