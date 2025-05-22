/**
 * NetSchool Admin Dashboard JavaScript
 */

// Initialize tooltips
document.addEventListener("DOMContentLoaded", () => {
  // Toggle sidebar on mobile
  const sidebarToggle = document.getElementById("sidebarToggle")
  const sidebarCollapseBtn = document.getElementById("sidebarCollapseBtn")
  const adminContainer = document.querySelector(".admin-container")

  if (sidebarToggle) {
    sidebarToggle.addEventListener("click", () => {
      document.body.classList.toggle("sidebar-mobile-open")
    })
  }

  if (sidebarCollapseBtn) {
    sidebarCollapseBtn.addEventListener("click", () => {
      adminContainer.classList.toggle("sidebar-collapsed")
    })
  }

  // Initialize tooltips if Bootstrap is available
  if (typeof bootstrap !== "undefined") {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))
  }

  // Task checkboxes
  const taskCheckboxes = document.querySelectorAll(".task-item .form-check-input")
  taskCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      const taskItem = this.closest(".task-item")
      if (this.checked) {
        taskItem.classList.add("completed")
      } else {
        taskItem.classList.remove("completed")
      }
    })
  })

  // Handle notifications
  const notificationItems = document.querySelectorAll(".notification-item")
  notificationItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      if (this.classList.contains("unread")) {
        this.classList.remove("unread")

        // Update notification count
        const notificationBadges = document.querySelectorAll(".action-btn .badge")
        notificationBadges.forEach((badge) => {
          const count = Number.parseInt(badge.textContent) - 1
          badge.textContent = count > 0 ? count : ""
          if (count <= 0) {
            badge.style.display = "none"
          }
        })
      }
    })
  })

  // Mark all notifications as read
  const markAllReadBtn = document.querySelector(".dropdown-header a")
  if (markAllReadBtn) {
    markAllReadBtn.addEventListener("click", (e) => {
      e.preventDefault()

      // Mark all notifications as read
      const unreadNotifications = document.querySelectorAll(".notification-item.unread")
      unreadNotifications.forEach((notification) => {
        notification.classList.remove("unread")
      })

      // Update notification count
      const notificationBadges = document.querySelectorAll(".action-btn .badge")
      notificationBadges.forEach((badge) => {
        badge.textContent = ""
        badge.style.display = "none"
      })
    })
  }
})
