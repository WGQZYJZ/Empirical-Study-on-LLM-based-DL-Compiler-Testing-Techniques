x = torch.randn(1, 3, 5)
torch.fft.rfftfreq(5)
np.testing.assert_array_almost_equal(torch.fft.rfftfreq(5).numpy(), np.fft.rfftfreq(5))