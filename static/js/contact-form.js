document.addEventListener('DOMContentLoaded', function() {
    const inquiryTypeField = document.getElementById('id_inquiry_type');
    const artworkFields = document.getElementById('artwork-fields');
    const contactFormToggle = document.getElementById('contactFormToggle');
    const contactFormCollapse = document.getElementById('contactFormCollapse');
    
    // Toggle artwork fields based on inquiry type (CUSTOM BUSINESS LOGIC)
    function toggleArtworkFields() {
        if (inquiryTypeField && artworkFields) {
            if (inquiryTypeField.value === 'purchase') {
                artworkFields.style.display = 'block';
            } else {
                artworkFields.style.display = 'none';
            }
        }
    }
    
    // Initial toggle for artwork fields
    toggleArtworkFields();
    
    // Toggle on change for artwork fields
    if (inquiryTypeField) {
        inquiryTypeField.addEventListener('change', toggleArtworkFields);
    }
    
    // Contact Form Collapse/Expand functionality
    if (contactFormToggle && contactFormCollapse) {
        const toggleLabel = document.getElementById('toggleLabel');
        
        // Function to update toggle text and states
        function updateToggleState(isExpanded) {
            if (toggleLabel) {
                toggleLabel.textContent = isExpanded ? 'Click to collapse' : 'Click to expand';
            }
        }
        
        // Handle the toggle button click
        contactFormToggle.addEventListener('click', function() {
            const isExpanded = contactFormToggle.getAttribute('aria-expanded') === 'true';
            const toggleIcon = document.getElementById('toggleIcon');
            
            // Update aria-expanded attribute for proper accessibility
            contactFormToggle.setAttribute('aria-expanded', !isExpanded);
            
            // Add visual feedback
            if (toggleIcon) {
                if (!isExpanded) {
                    toggleIcon.style.transform = 'rotate(180deg)';
                } else {
                    toggleIcon.style.transform = 'rotate(0deg)';
                }
            }
            
            // Update text immediately for better UX
            updateToggleState(!isExpanded);
        });
        
        // Listen for Bootstrap collapse events
        contactFormCollapse.addEventListener('shown.bs.collapse', function() {
            contactFormToggle.setAttribute('aria-expanded', 'true');
            updateToggleState(true);
        });
        
        contactFormCollapse.addEventListener('hidden.bs.collapse', function() {
            contactFormToggle.setAttribute('aria-expanded', 'false');
            updateToggleState(false);
        });
        
        // Initialize the correct state on page load
        updateToggleState(false);
    }
});