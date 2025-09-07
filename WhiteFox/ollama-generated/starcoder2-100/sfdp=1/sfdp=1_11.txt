

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value, dropout_p=0.75, inv_scale_factor=8):  # We do not need to specify dropout because it is randomly initialized at the start of training and thus does not affect our search
        v1 = torch.matmul(query, key.transpose(-2, -1)) 
        v2 = v1 / inv_scale_factor
        v3 = self.softmax(v2)  # Note that this line can be replaced by torch.nn.functional.softmax() to make the pattern more concise
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) 
        v5 = dropout_qk.matmul(value) 
        return v6


# Initializing the model 
m  = Model()

# Inputs for the model  
q1, k2, v3 = torch.randn(2048, 768), torch.randn(2048, 768), torch.randn(768, 2048)

 # Initializing the initial model's input tensor:
x1  = m(q1, k2, v3)

# Initializing the target model's input tensors as a new set of input tensors. Each of them has size (512 x 64), and the last 8 dimensions correspond to channels.
x2s_i  = [torch.randn(size=(int(8 * 3072 / 16) - 9, 8))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x2s_t  = [torch.randn(size=(int(8 * 7 / 16) - 9, 8))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x2_t  = x2s_i[0] + torch.randn((int(8 * 7 / 16), 8)) # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x2s_a  = [torch.randn((int(107 / 2) - 9, 8))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x2s_b  = [torch.randn((int(7 / 2) - 9, 8))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x2s_c  = [torch.randn((int(7 / 2) - 9, 8))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example

# Initializing the target model's input tensor:
x3s_i = [torch.randn((int(8 * 7 / 2) - 9, 10)) for _ in range(len(x2s_a))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x3s_a = [torch.randn((int(7 / 2) - 9, 10)) for _ in range(len(x2s_i))] # Note that we cannot use torch.rand(size=(512, 64)), because the number of 8-channel tensors is not divisible by 3 in this example
x3 = x3s_i[0] + x3s_a[0]

 