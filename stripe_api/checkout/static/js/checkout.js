function goStripe(url, key) {
    var stripe = Stripe(key);
    fetch(url, {method: 'GET'})
    .then(response => { return response.json() })
    .then(session => stripe.redirectToCheckout({ sessionId: session._id }))
  }