
class Model(torch.nn.Module):
    def __init__(self, in1):
        super().__init__()
        self.linear  = torch.nn.Linear(2*in1 + 2, 4)

    def forward(self, x1, x2):
        # A
        v01a  = x1.permute(0, 2, 1).contiguous()  # Permuted tensor A with more than two dimensions and 'permute' method is invoked first.
        v02a  = torch.nn.functional.linear(v01a, self.linear.weight)

        # B
        v03b  = x2.permute(0, 2, 1).contiguous()  # Permuted tensor B with more than two dimensions and 'permute' method is invoked first.
        v04b  = torch.nn.functional.linear(v03b, self.linear.weight)

        # C (1)
        v05a = input_tensorA.permute(...)   # Input tensors A is permuted twice in this scenario.
        v06a = input_tensorB.permute(...)
        v07c = torch.nn.functional.bmm(v04b, t3)

        return v02a + v05a, v06a, v07c


# Initializing the model 
m  = Model(input_sizeA) # input size of A is input_sizeA

