let preTarget = document.querySelector(`#header a[href*="${location.hash}"]`) || document.querySelector('#header a')

preTarget.dataset.active = 'true'

document.querySelector('#header').addEventListener('click', (event) => {
  const target = event.target

  if (target.tagName.toLowerCase() !== 'a') {
    return
  }

  delete preTarget.dataset.active
  preTarget = target

  target.dataset.active = 'true'
})
