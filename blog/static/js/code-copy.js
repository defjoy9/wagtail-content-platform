// Add copy buttons to code blocks and handle Notion-style code paste
document.addEventListener('DOMContentLoaded', function() {
    // Find all code blocks
    const codeBlocks = document.querySelectorAll('.markdown-content pre');
    
    codeBlocks.forEach(function(pre) {
        // Create wrapper for macOS window styling
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        
        // Create macOS-style header with traffic lights
        const header = document.createElement('div');
        header.className = 'code-block-header';
        
        const trafficLights = document.createElement('div');
        trafficLights.className = 'traffic-lights';
        trafficLights.innerHTML = `
            <span class="traffic-light traffic-light-red"></span>
            <span class="traffic-light traffic-light-yellow"></span>
            <span class="traffic-light traffic-light-green"></span>
        `;
        
        // Create copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.5 4.5H2.5C2.22386 4.5 2 4.72386 2 5V13.5C2 13.7761 2.22386 14 2.5 14H10.5C10.7761 14 11 13.7761 11 13.5V10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <rect x="5.5" y="2" width="8" height="8" rx="0.5" stroke="currentColor" stroke-width="1.5"/>
            </svg>
            <span>Copy</span>
        `;
        copyButton.setAttribute('aria-label', 'Copy code to clipboard');
        
        header.appendChild(trafficLights);
        header.appendChild(copyButton);
        
        // Wrap the pre element
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(header);
        wrapper.appendChild(pre);
        
        // Add copy functionality
        copyButton.addEventListener('click', function() {
            const code = pre.querySelector('code');
            const text = code ? code.textContent : pre.textContent;
            
            navigator.clipboard.writeText(text).then(function() {
                // Show success feedback
                const originalHTML = copyButton.innerHTML;
                copyButton.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3 8L6.5 11.5L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>Copied!</span>
                `;
                copyButton.classList.add('copied');
                
                setTimeout(function() {
                    copyButton.innerHTML = originalHTML;
                    copyButton.classList.remove('copied');
                }, 2000);
            }).catch(function(err) {
                console.error('Failed to copy code: ', err);
            });
        });
    });
});
