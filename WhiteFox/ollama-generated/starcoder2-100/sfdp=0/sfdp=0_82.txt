

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=0.1):
        super().__init__()
        self.key = torch.nn.Linear(768)  # Number of keys and query vectors is the same
        self.query = torch.nn.Linear(768)

    def forward(self, input1, input2): 
        # Scaling factor is applied to the dot product
        scaled_dot_product = torch.matmul(input1, self.key.weight.transpose(-2, -1)) / math.sqrt(inv_scale)

        attention_weights = scaled_dot_product.softmax(dim=-1)  # Softmax of the dot product of query and key tensors
        output = torch.matmul(attention_weights, input2)  # Weighted sum of value tensor using weights computed from Scaled Dot-Product Attention
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.attn1 = ScaledDotProductAttention()
        self.attn2 = ScaledDotProductAttention()
        self.attn3 = ScaledDotProductAttention()
        self.attn4 = ScaledDotProductAttention()

        # All parameters must be trainable
        for m in self.modules():
            if isinstance(m, torch.nn.Linear):
                nn.init.xavier_uniform_(m.weight)

    def forward(self, input1):
        out1  = self.attn1(input1, input1)[0] + input1

        out2  = self.attn2(out1, input1)[0] + out1

        out3  = self.attn3(out2, input1)[0] + out2

        out4  = self.attn4(out3, input1) # [input_size, batch_size, sequence_length, hidden size ]
        return torch.transpose(out4[::-1], -1,-2)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(30, 512)

# Predicted output of the model from the inputs provided above
__output__  = m(x1)

<div class="alert alert-block alert-success">
<b>SUCCESS!</b> The output is generated successfully!
</div>