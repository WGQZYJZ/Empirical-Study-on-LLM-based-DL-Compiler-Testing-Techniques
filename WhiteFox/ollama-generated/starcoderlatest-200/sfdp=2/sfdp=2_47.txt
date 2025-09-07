
class Model(torch.nn.Module):
    def __init__(self,
                 hidden_size=128,
                 head_num=16,
                 num_layers=2,
                 output_dim=1,
                 activation='softmax'):
        super().__init__()
 
        self.output_linear = torch.nn.Linear(hidden_size * 3, output_dim)
 
    def forward(self, x):
        qk = self.multihead_attention(x, x, x, head_num)
        out = v + k + q  # linear transformation of 3 hidden dim tensors 
        return self.output_linear(out)
 
    def multihead_attention(self, query, key, value, num_heads):
        batch_size = query.shape[0]
 
        hidden_dim = int(hidden_dim / num_heads)
        scale_factor = 1 / math.sqrt(scale_factor)
 
        out = torch.einsum('b i j n d -> b (i d) j', (query, key))
        out *= scale_factor
        out += scale_factor
        softmax_out = F.softmax(out, dim=-1)
        dropout_softmax_out = self.dropout(softmax_out, p=dropout_p)
 
        attention_output = torch.einsum('b (i d) j -> b i j', (dropout_softmax_out, value))
        attention_output *= scale_factor
        return attention_output
 
    def get_multihead_attention(self):
        # hidden_dim: 128 * 3 / num_heads = 40
        head_num = 16

        key = torch.nn.Sequential(
            torch.nn.Linear(hidden_size, hidden_dim),
            self.dropout,
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim * num_heads),
            torch.nn.Unfold(2, padding=1),
            torch.nn.permute((0, 3, 2, 1))
        )
 
        value = torch.nn.Sequential(
            key,
            torch.nn.Linear(hidden_size, hidden_dim * num_heads),
            torch.nn.Unfold(2, padding=1),
            torch.nn.permute((0, 3, 2, 1))
        )
 
        query = torch.nn.Sequential(
            key,
            torch.nn.Linear(hidden_size, hidden_dim * num_heads),
            torch.nn.Unfold(2, padding=1),
            torch.nn.permute((0, 3, 2, 1))
        )
 
        return self.multihead_attention
 
    def forward(self, query, key, value):
        softmax_out = F.softmax(out, dim=-1)
        dropout_softmax_out = self.dropout(softmax_out, p=dropout_p)

        attention_output = torch.einsum('b (i d) j -> b i j', (dropout_softmax_out, value))
        attention_output *= scale_factor
        return attention_output

# Model with multi-head attention layer and linear transformation
model_multihead_attention = Model()
m1 = model_multihead_attention(query, key, value)


# Model with single-head attention layer and additive gate
class AttentionLayer(torch.nn.Module):
    def __init__(self, hidden_size=64, output_dim=2):
        super().__init__()
 
        self.output_linear = torch.nn.Linear(hidden_size * 3, output_dim)
 
    def forward(self, x1, query):
        attention = torch.einsum('b i j n d -> b (i d) j', (query, key))
        return self.output_linear(attention)
 

class Model(torch.nn.Module):
    def __init__(self, attention=AttentionLayer):
        super().__init__()
 
        self.attention = attention
 
    def forward(self, x1, query):
        qk = self.attention()(x1, query)
 


# Inputs to the model with multi-head attention layer and linear transformation
x1 = torch.randn(32, 64, 64)
query = torch.randn(32, 20, 8 * 8)
m2 = m1 + m1
