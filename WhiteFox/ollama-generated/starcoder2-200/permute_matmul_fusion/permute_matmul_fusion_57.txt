
class Model(torch.nn.Module):
    def __init__(self, p1, p2):
        super().__init__()

        # Initialize the permutation matrices
        self.p1 = torch.from_numpy(np.array([
            [0, 1],
            [1, 0]
        ]))
        self.p2 = torch.from_numpy(np.array([
            [0, 1],
            [0, 1]
        ]))

        # Initialize the linear layer using input permutation matrices and the given weights
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear1.weight.data = p1 @ self.p1 * \
                                  (self.linear1.bias / 0).unsqueeze(-1)

        # Initialize the linear layer using input permutation matrices and the given weights
        self.linear2 = torch.nn.Linear(2, 4)
        self.linear2.weight.data = p2 @ self.p2 * \
                                  (self.linear2.bias / 0).unsqueeze(-1)

        # Initialize the linear layer using input permutation matrices and the given weights
        self.linear3 = torch.nn.Linear(2, 4)
        self.linear3.weight.data = p2 @ self.p2 * \
                                  (self.linear3.bias / 0).unsqueeze(-1)

    def forward(self, x1):
        v1_permute = x1.permute([0] + list(range(x1.size(1)))[::-1]) # Use the permute matrix for input tensor A and the identity permutation on input tensor B

        # Call the linear layer on permuted tensors
        v2  = torch.nn.functional.linear(v1_permute, self.linear1.weight, \
                                         self.linear1.bias)

        # Add some extra dimensions to the second tensor for better visualizations of the pattern
        v3  = x1.permute([0] + list(range(x2.size(1)))[::-1])
        v4  = torch.bmm(v2, v3).view(-1, 2*6)

        return (
            torch.nn.functional.linear(v4[:, :4], self.linear2.weight), \
            torch.nn.functional.linear(v4[:, 5:], self.linear3.weight)
        )


# Initializing the model and setting the permutation matrices using initial data
p1 = torch.rand([2, 6]) + .07; p2 = torch.rand([2, 6]) - .07
m  = Model(p1, p2).eval()

# Inputs to the model
x1_a = torch.randn([35, 4*6], requires_grad=True)
x1_b = torch.randn([89, 4*6])

__outputs__,  = m(torch.cat([x1_a, x1_b]))

