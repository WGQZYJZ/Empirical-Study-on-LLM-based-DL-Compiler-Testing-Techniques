
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.tensor([[0., 0., 0., 1., 0.], [0., 0., 0., 1., 0.], [0., 0., 0., 1., 0.],
                                        [1., 0., 0., 1., 1.], [0., 0., 1., 1., 0.]], dtype=torch.float32)
        self.query = torch.tensor([[[[1., 2., 3.], [4., 5., 6.]]], [[[7., 8., 9.]]]])
        self.key = torch.tensor([[[[-1, -2, -3], [-4, -5, -6.]], [[-7, -8, -9.]]]])
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return attn_weight @ self.key


# Test code
import timeit
def run_benchmark(num_iter=1):
    start = timeit.default_timer()
    
    for i in range(num_iter):
        __output__  = m(__input__)
        
    end = timeit.default_timer()

    return (end - start) / num_iter, end


